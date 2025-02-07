# Number Classification API

## Overview
The **Number Classification API** is a RESTful API that receives a number and returns its mathematical properties, including:
- Whether it is prime or perfect.
- Whether it is even or odd.
- Whether it is an Armstrong number.
- The sum of its digits.
- A fun fact about the number using the [Numbers API](http://numbersapi.com/).

The API is deployed on **AWS Lambda** and exposed using **AWS API Gateway**.

## Features
- Classifies numbers based on mathematical properties.
- Provides a fun fact about the number.
- Uses AWS Lambda for a serverless deployment.
- Handles **CORS** for cross-origin requests.
- Returns responses in JSON format.

---
## API Specification
### **Endpoint:**
```
GET https://{api-gateway-id}.execute-api.{region}.amazonaws.com/prod/api/classify-number?number=371
```

### **Request Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| number | Integer | The number to classify |

### **Response Format (200 OK):**
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "armstrong",
    "odd"
  ],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}
```

### **Response Format (400 Bad Request):**
```json
{
    "number": "alphabet",
    "error": true
}
```

---
## Deployment
### **1. Clone the Repository**
```bash
git clone https://github.com/Goodluck101/numberFunFactAPI.git
cd number-classifier-api
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Package the Project for AWS Lambda**
```bash
mkdir package && cd package
pip install --target="." -r ../requirements.txt
cp ../lambda_function.py .
zip -r ../deployment.zip .
cd ..
```

### **5. Upload to AWS Lambda**
```bash
aws lambda create-function \
    --function-name number-classifier-api \
    --runtime python3.10 \
    --role arn:aws:iam::your-account-id:role/your-lambda-role \
    --handler lambda_function.lambda_handler \
    --timeout 14 \  # Use 10 to 15 seconds
    --memory-size 128 \
    --zip-file fileb://deployment.zip
```

### **6. Set Up API Gateway**
```bash
aws apigateway create-rest-api --name "NumberClassifierAPI"
```

#### **Connect API Gateway to Lambda**
```bash
aws apigateway put-integration \
  --rest-api-id {api-gateway-id} \
  --resource-id {resource-id} \
  --http-method GET \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/arn:aws:lambda:{region}:{account-id}:function:number-classifier-api/invocations
```

### **7. Deploy the API Gateway**
```bash
aws apigateway create-deployment --rest-api-id {api-gateway-id} --stage-name prod
```

### **8. Grant API Gateway Permission to Invoke Lambda**
```bash
aws lambda add-permission \
    --function-name number-classifier-api \
    --statement-id apigateway-access \
    --action lambda:InvokeFunction \
    --principal apigateway.amazonaws.com
```

### **9. Retrieve API Gateway URL**
```bash
aws apigateway get-rest-apis
```
Use the API Gateway **invoke URL** for testing.

---
## Testing
### **Using Curl**
```bash
curl -X GET "https://{api-gateway-id}.execute-api.{region}.amazonaws.com/prod/api/classify-number?number=371"
```

### **Using Postman**
- Set method to **GET**
- Enter the API URL with a valid number
- Click **Send**

---
## Error Handling
| Error | Cause | Resolution |
|-------|-------|------------|
| `"message": "Missing Authentication Token"` | Incorrect API Gateway URL | Verify the endpoint URL and stage |
| `"message": "Not Found"` | Route not properly mapped | Check resource paths in API Gateway |
| `Runtime.ImportModuleError` | Missing dependencies in Lambda | Ensure all dependencies are in `deployment.zip` |

---
## Technologies Used
- **Python** (FastAPI framework)
- **AWS Lambda** (Serverless compute)
- **AWS API Gateway** (Routing API requests)
- **Numbers API** (Fetching fun facts)

---
## Author
**Goodluck Adiole**

---
## License
This project is open-source and available under the **MIT License**.

