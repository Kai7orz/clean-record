type ImageResponse = { record_id:number, image_id:number, image_url:string, image_description:string }[]

export default defineEventHandler(async (event) => {
    console.log("called getImages.ts")
    const data = await $fetch<ImageResponse>('http://fast_api:8000/users/1');
  
    console.log("images :: ",data)
    console.log("images の type は", typeof data)
    return data 
})