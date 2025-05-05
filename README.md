# Celica Identity Verification

A secure, fast identity verification system with face recognition, document verification, and phone verification.

## Features

- **Face Verification**: Uses InsightFace for accurate face recognition and matching.
- **Document Verification**: Extracts information from ID documents and matches face with selfie.
- **Phone Verification**: Secures accounts with 2FA using SMS verification codes.
- **User Management**: Stores verified users with face embeddings in a FAISS vector database.
- **Frontend SDK**: Simple JavaScript SDK for integrating with websites.

## Architecture

The system follows a multi-stage verification flow:

1. **Phone Verification**: User enters phone number and verifies with OTP.
2. **Face Verification**: User takes a selfie for verification.
3. **Document Verification**: User uploads ID document, which is matched with selfie.
4. **User Creation/Authentication**: User is created or authenticated based on verification results.

## Setup

### Prerequisites

- Python 3.8+
- Redis
- PostgreSQL (optional, SQLite is used by default)
- Tesseract OCR

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/celica.git
   cd celica
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export REDIS_URL=redis://localhost:6379
   export DATABASE_URL=postgresql://user:password@localhost/celica
   export JWT_SECRET=your-secret-key
   
   # For Twilio (optional)
   export TWILIO_ACCOUNT_SID=your-account-sid
   export TWILIO_AUTH_TOKEN=your-auth-token
   export TWILIO_PHONE=your-twilio-phone
   
   # For S3 (optional)
   export S3_BUCKET=your-bucket-name
   export AWS_ACCESS_KEY_ID=your-access-key
   export AWS_SECRET_ACCESS_KEY=your-secret-key
   ```

### Running the Application

1. Start the development server:
   ```
   python -m celica.api.app
   ```

2. For production, use Gunicorn:
   ```
   gunicorn -w 4 -b 0.0.0.0:5000 celica.api.app:app
   ```

## Frontend Integration

Include the Celica SDK in your website:

```html
<script src="https://cdn.celica.id/sdk.js"></script>
<div id="celica-login-button"></div>

<script>
    const celica = Celica.init('YOUR_CLIENT_ID', {
        onAuth: function(result) {
            if (result.success) {
                console.log('User authenticated:', result.user);
                // Handle successful authentication
            } else {
                console.error('Authentication failed:', result.error);
                // Handle authentication failure
            }
        }
    });
</script>
```

## API Documentation

### Authentication Endpoints

- `POST /api/send-otp`: Send OTP to phone number
- `POST /api/verify-otp`: Verify OTP and create session
- `POST /api/verify-face`: Verify user's face
- `POST /api/verify-document`: Verify ID document and match with face
- `POST /api/callback`: Handle callback for client applications

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security Considerations

This system handles sensitive personal information. Always:

1. Use HTTPS in production
2. Store sensitive data securely
3. Follow data protection regulations (GDPR, CCPA, etc.)
4. Implement proper access controls
5. Regularly audit security practices 