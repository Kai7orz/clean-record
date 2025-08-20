type RecordType = {
    user_id: number 
    category_id: number
    record_name: string
    image_url: string 
    image_description: string 
}

export default defineEventHandler( async (event) => {

    const body = await readBody(event) 
    const{ userId , categoryId , recordName, imageUrl, imageDescription } = body
    const url = 'http://fast_api:8000/users/' + userId + "/records/images"
    const postData:RecordType = {
        user_id: userId ,
        category_id: categoryId,    
        record_name: recordName,
        image_url: imageUrl,  
        image_description: imageDescription,
    }

    const res = await fetch(url,{
        method: 'POST',
        headers: {
                  'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
    })

    console.log("image insert error　時にresposne がどのように変えるか見てみる",res)

})