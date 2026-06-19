# PlacePro AI API Design

## Authentication APIs

### Register User

POST /api/auth/register

Request:

{
"name": "Prajjwal Singh",
"email": "[user@email.com](mailto:user@email.com)",
"password": "password123"
}

Response:

{
"message": "User registered successfully"
}

---

### Login User

POST /api/auth/login

Request:

{
"email": "[user@email.com](mailto:user@email.com)",
"password": "password123"
}

Response:

{
"token": "jwt_token"
}

---

## Resume APIs

### Upload Resume

POST /api/resume/upload

Response:

{
"resume_score": 82,
"skills": [],
"projects": [],
"certifications": []
}

---

## Placement Prediction APIs

POST /api/predict-placement

Response:

{
"placement_probability": 85
}

---

## Interview APIs

POST /api/interview/start

POST /api/interview/answer

GET /api/interview/result

---

## Roadmap APIs

POST /api/roadmap/generate

Response:

{
"roadmap_type": "30_day_plan"
}

---

## Analytics APIs

GET /api/analytics/dashboard
