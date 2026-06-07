document.getElementById("loginForm").addEventListener("submit", function(e){
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const message = document.getElementById("message");

    if(username === "" || password === ""){
        message.style.color = "red";
        message.innerText = "All fields are required!";
        return;
    }

    if(username === "admin" && password === "admin123"){
        message.style.color = "green";
        message.innerText = "Login Successful!";
    } else {
        message.style.color = "red";
        message.innerText = "Invalid Username or Password!";
    }
});
