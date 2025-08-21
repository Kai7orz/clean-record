type CategoryType = {
    category_name: string
}

export default defineEventHandler( async (event) => {
    const body = await readBody(event)
    console.log("BODY ->",body) 
    const { categoryName} = body 
    const url = 'http://fast_api:8000/categories'
    const postData:CategoryType = {
        category_name: categoryName
    }
    console.log("POST DATA:",postData)
    const _res = await fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
})