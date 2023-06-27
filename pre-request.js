pm.request.headers.add({key: 'Content-Type', value: 'application/vnd.api+json'});

const postRequest = {
    url: "https://adminapi.pay.junction.dev/users/tokens",
    method: "POST",
    header:  {"Content-Type" : "application/vnd.api+json"},
    body: {
    mode: "raw",
    raw: {
        "data": {
        "type": "user-tokens",
        "attributes": {
            "email": "email@email.com",
            "password": "password"
        }
    }
 }
    }
};

pm.sendRequest(postRequest, function (err, response) {
    console.log(response.json());
    console.log(response.json()["errors"]);
    pm.environment.set("NEW_TOKEN", response.json()["data"]["id"]);

// pm.request.headers.add({"Content-Type": "application/vnd.api+json"});

   // pm.globals.set("Content-Type", "application/vnd.api+json");
});
