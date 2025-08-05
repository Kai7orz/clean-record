type MyApiResponse = { 
    user_id : number,
    user_name: string ,
}[]

export default defineEventHandler(async (event) => {
    try{
        const data = await $fetch<MyApiResponse>('http://fast_api:8000')
        console.log(data[0].user_id,data[0].user_name)
        return data 
    } catch (error) {
        console.error("failed to fetch data --> ",error)
        return {error: 'ユーザー取得に失敗'}
    }
})