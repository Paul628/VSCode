const { scryptSync, randomBytes, timingSafeEqual } = require('crypto');

users = []

function signup(email, password){
    const salt = randomBytes(16).toString('hex');
    const hashedPassword = scryptSync(password, salt, 64).toString('hex')

    const user = { email, password: `${salt}:${hashedPassword}`}

    users.push(user);

    return user

}

function login(email, password){
    const user = users.find(v => v.email === email);
    if(!(user == null)){
        const[salt, key] = user.password.split(':');
        const hashedBuffer = scryptSync(password, salt, 64);

        const keyBuffer = Buffer.from(key, 'hex');
        const match = timingSafeEqual(hashedBuffer, keyBuffer);

        if (match){
            console.log("success");
            return 'login success'
            
        }
        else{
            console.log("fail");
            return 'login fail!'
        }
    }
    console.log("User not in database");
    return "User not in database"
}




signup("paul", "passwort");

signup("jan", "passwort123");

//console.log(users);

//login("paul", "password")

//login("paull", "passwort")

login("paul", "passwort")

