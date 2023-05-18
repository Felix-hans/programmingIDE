curl --progress-bar \
        --no-silent \
        -X POST \
        -H "Content-Type: application/json" \
        -H "X-RapidAPI-Key: 9e1ba1c6c2msh0a52d32b789b21fp1bff69jsn8b2f64d2a2f9" \
        -H "X-RapidAPI-Host: judge0-ce.p.rapidapi.com" \
        --data @request_body.json \
        --output request_response.json \
        "$JUDGE0_CE_BASE_URL/submissions?base64_encoded=true&wait=false"