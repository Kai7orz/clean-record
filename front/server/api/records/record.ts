type RecordType = {
    user_id: number 
    category_id: number
    record_name: string
}

export default defineEventHandler( async (event) => {

    const body = await readBody(event) 
    const{ userId , categoryId , recordName } = body
    const url = 'http://fast_api:8000/users/' + userId + "/records"
    const postData:RecordType = {
        user_id: userId ,
        category_id: categoryId,    
        record_name: recordName,
    }

    console.log("postData->",postData)
    const res = await fetch(url,{
        method: 'POST',
        headers: {
                  'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
    })
})