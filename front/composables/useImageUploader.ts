export const useImageUploader = async (recievedFile: File)=>{
    // ts ではDOM にアクセスできないため，DOM 情報はこの呼び出し元のコンポーネントが取得して，props として渡す
    const file = recievedFile 
    const url = "/api/proxy";

    if(!file) return 
    // Input のデータを読み込んだ後に，FormData オブジェクトを生成する
    const formData = new FormData() 
    formData.append('ufile',file) 
    // 生成したFormData オブジェクトをAPI Route へ送信する
    try{
        const res = await fetch('/api/proxy',{
            method: "POST",
            body: formData,
        })

    // データ送信後にレスポンス受信成功した際の処理
        if(res.ok){
            const imageUrl = await res.json(); 
            return imageUrl
        } else {
            console.error("No Responses : ",res.status);
        }
    } catch(err) {
        console.error("Failed to POST or Receive Response : ",err);
    }
}