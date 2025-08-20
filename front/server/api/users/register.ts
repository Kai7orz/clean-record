type RegisterType = {
    user_name: string 
    email: string 
    age: string
}

export default defineEventHandler(async (event) => {
    const body = await readBody(event)
    const { userName,userEmail,ageString } = body

    const url = 'http://fast_api:8000/users/register'
    const postData:RegisterType = {
        user_name : userName,
        email : userEmail,
        age : ageString,
    }

    console.log("body -> ",JSON.stringify(postData))
                       
    const res = await fetch(url,{
        method: 'POST',
        headers: {
                  'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
    })
});