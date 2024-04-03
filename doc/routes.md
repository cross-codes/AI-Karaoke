<div align="center">
<h1>🎤 AI-Karaoke-Backend</h1>

An API built for the AI-Karaoke event

</div>

---

## Possible error responses

|Error serial| Status code | Response Body (Plain JSON) |
|:----------:|:-----------:|:-------------:|
|E1        |500          |{ "error": "string" }|

## Routes

Henceforth the term `{{url}}` will refer to the URL on which the API is hosted.

Eg: In the case of a local deployment, `{{url}}` will be `https:/localhost:8000`

---
(1) **`GET`** `{{url}}/health`

**Expected Request Body**: N/A

**Successful response**: Accompanied by a 200 (OK) status code:

```JSON
{
    "message": "Server is active"
}
```

(2) **`GET`** `{{url}}/training`

**Expected Request Body**: N/A

**Successful response**: Accompanied by a 200 (OK) status code:

```JSON
{
    "message": "Model Training complete"
}
```

**Potential errors**:

Type `E1` if the model training failed

(3) **`POST`** `{{url}}/prediction/`

**Expected Request Body**: Plain JSON ; Must have an accessible `data` field:

```JSON
{
    "...",
    "data": ["<string, 1>", "<string, 2>", "<string, 3>"],
    "..."
}
```

**Successful response**: Accompanied by a 200 (OK) status code:

```JSON
{
    "data": [
        "<Integer 1>",
        "<Integer 2>",
        "<Integer 3>"
    ],
    "prediction": [
        "<string, 4>",
        "<string, 5>",
        "<string, 6>",
        "<string, 7>"
    ]
}
```

**Potential errors**:

For this request:

* String 1 should be one of `Happy` or `Sad`
* String 2 should be one of `High`, `Medium` or `Low`
* String 3 should be one of `Fast`, `Mid-tempo` or `Slow`
* String 4 - 7 will be quoted strings that are song recommendations

If any of these specifications are not met, an error of type `E1` will be
encountered with a relevant message

---

## Note

To use the model, first send a GET request to `/training`, and then send the
POST request to `/prediction`, to ensure unique responses every time.
