type ImageResponse = { record_id:number, image_id:number, image_url:string, image_description:string }[]

export default defineEventHandler(async (event) => {
    const body = await readBody(event) 
    const  { userId }  = body 
    const data = await $fetch<ImageResponse>('http://fast_api:8000/users/'+userId);
    return data 
})