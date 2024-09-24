import torch
import torch.nn.functional as functional
from transformers import AutoTokenizer, AutoModelForSequenceClassification #, BertModel, BertTokenizer
from torch.utils.data import TensorDataset, DataLoader # RandomSampler #, SequentialSampler

from flask_classful import FlaskView, route, request
from flask import Flask, request, jsonify
import json

class TextPredictor(FlaskView):
    route_base = '/'

    def __init__(self) -> None:
        fp = open('predictor.config')
        self.config = json.load(fp)
        fp.close()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer, self.model = self.load_model()

    @route('/predict', methods=['POST'])
    def predict(self):
        message = request.get_json(force=True)
        input_text = message['input_text']

        prediction = self.model_prediction(input_text, True)

        prediction = {str(key): str(value) for key, value in prediction.items()}
        return jsonify(prediction)

    def model_prediction(self, data, convert_output_to_probability):
        
        # Prepare the test dataset
        dataloader_test = self.prepare_dataset([data], shuffle=False)

        self.model.eval()
        
        # loss_val_total = 0

        j = 0  # Index for accessing rows in the DataFrame

        for batch in dataloader_test:
            batch = tuple(b.to(self.device) for b in batch)       
            
            inputs = {
                'input_ids': batch[0],
                'attention_mask': batch[1]
            }

            with torch.no_grad():
                outputs = self.model(**inputs)

            print(outputs)
            # loss = outputs[0]
            # loss_val_total += loss.item()
            logits = outputs.logits#[1]

            if convert_output_to_probability:
                logits = functional.softmax(logits, dim=-1)

            if self.device == 'cuda':    
                logits = logits.detach().cpu().numpy()
            else:
                 logits = logits.detach().numpy()[0]
        
        labels_names = list(self.model.config.id2label.values())

        predictions = {label: logits[i] for i, label in enumerate(labels_names)}
             
        return predictions

    def prepare_dataset(self, data, shuffle=True):
        
        # Tokenize the dataset to get input IDs and attention masks
        input_ids, att_masks = self.tokenize_dataset(data)

        # Move tensors to the specified device (GPU or CPU)
        input_ids = input_ids.to(self.device)
        att_masks = att_masks.to(self.device)
        
        # Create a TensorDataset from the input IDs, attention masks, and labels
        dataset = TensorDataset(input_ids, att_masks)

        # Create a DataLoader for batching the dataset
        data_loader = DataLoader(dataset, batch_size=32, shuffle=shuffle)

        return data_loader  # Return the DataLoader

    def tokenize_dataset(self, data, max_length=128):
        
        # Use the tokenizer to encode the data
        encoded_dict = self.tokenizer.batch_encode_plus(
            data,
            add_special_tokens=True,
            max_length=max_length,
            padding='max_length',
            return_attention_mask=True,
            truncation=True,
            return_tensors='pt'
        )

        return encoded_dict['input_ids'], encoded_dict['attention_mask']  # Return the input IDs and attention masks


    def load_model(self):

        model_name = self.config['model_name']

        # Load the tokenizer from the pre-trained model
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Load the model from the pre-trained model
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        # Move the model to the specified device (e.g., GPU or CPU)
        model.to(self.device)

        return tokenizer, model


app = Flask(__name__)
TextPredictor.register(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)