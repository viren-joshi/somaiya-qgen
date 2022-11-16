function bookmarkQuestion(qID,uID){
    // This API here works just like upvote/downvote api @taaha
    

    var bkmk = document.getElementById(`bkmk-${id}`);
    var data = {
        "question_id": id,
        "user_id": 1,
    }
    const url = "taaha.pls.send.url";
    if (thumb.classList.contains('bi-bookmark-fill')) {
        data["function"] = "remove_bookmark";
        const other_params = {
            method: "POST",
            mode: "cors",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        console.log(other_params);
        fetch(url, other_params)
            // "bi bi-hand-thumbs-up-fill"
            .then(function (response) {
                console.log(response)
                if (response.ok) {
                    console.log("Bookmark Removed :)");
                    // refresh();
                    thumb.classList.remove("bi-bookmark-fill");
                    thumb.classList.add("bi-bookmark");
                } else {
                    throw new Error("Could not reach the API: " + response.statusText);
                }
            }
            )

    } else {
        data["function"] = "add_bookmark";
        const other_params = {
            method: "POST",
            mode: "cors",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
        console.log(other_params);
        fetch(url, other_params)
            // "bi bi-hand-thumbs-up-fill"
            .then(function (response) {
                console.log(response)
                if (response.ok) {
                    console.log("Question Bookmarked :)")
                    // refresh();
                    thumb.classList.remove("bi-bookmark");
                    thumb.classList.add("bi-bookmark-fill");
                } else {
                    throw new Error("Could not reach the API: " + response.statusText);
                }
            }
            )
    }
}

function doesSmth(){
    print("hello");
}