export default defineEventHandler(async (event) => {
  const files = await readMultipartFormData(event);
  const body = files?.[0];

  if (!body){
    throw createError({ statusCode: 400, message: "File is not provided."});
  }

  const formData = new FormData(); 
  formData.append("ufile",new Blob([body.data]),body.filename);

  // console.log("formData:",formData);

  const res = await fetch("http://fast_api:8000/users/1/", {
    method: 'POST',
     body: formData
  });
  
  const response = await res.json();
  console.log("proxy->",response);
  return response 
});
