# kasada solver api

https://discord.gg/kasada

# API Pricing for Captcha Solving Service

## Pricing Structure

- **Cost**: $0.10 per 1,000 requests
  - Each request processed through the API costs $0.0001.

### Example Pricing Breakdown

```  Number of Requests   Cost ($)  
|--------------------|----------|
| 1,000              | 0.10     |
| 10,000             | 1.00     |
| 100,000            | 10.00    |
| 1,000,000          | 100.00   |
|--------------------|----------|
```
## Cashback Program for Developers

If you use an **affiliate ID** when making requests through the API, you will receive a **5% cashback** on the cost associated with requests made from that affiliate account. 

### Cashback Example

- **Total Requests**: 10,000
- **Total Cost**: $1.00
- **Cashback Earned**: 5% of $1.00 = $0.05

### Important Notes
- Cashback is credited to the developer's account associated with the affiliate ID.
- Cashback can be used for future API requests
- Ensure that your API requests include your affiliate ID to qualify for the cashback.



# API Documentation

## Base URL
`http://liveboost.net/v1/`

---

## Endpoints

### 1. **POST /solv**

#### Description
This endpoint is used to solve a **passport** captcha

#### Request
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
      "api_key": "your_api_key",
      "app_id": your_app_id  // Optional
  }```

#### Response
- **Body**:
```json
{
      "captcha": {"client": "", "device": "", "integrity": "", "type": "", "useragent": ""}, 
      "success": true
}
```

### 2. **POST /balance**

#### Description
This endpoint retrieves the balance of a user

#### Request
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
      "api_key": "your_api_key",
  }```

#### Response
- **Body**:
```json
{
      "balance": 1.0, 
      "success": true
}
```

# ⚠️  API supports only Twitch, but we plan to add support for Nike and Kick in the future.

tags: 
X-Kpsdk-Ct
X-Kpsdk-H
X-Kpsdk-Fc
X-Kpsdk-H
x-kpsdk-dv
/fp
.ips




