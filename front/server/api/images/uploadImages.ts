export default defineEventHandler( async (event) => {
    // 受信したファイルをアップロードする
    const form = await readFormData(event)
    const file = form.get('file') as File

    ensureBlob(file, {
    maxSize: '1MB',
    types: ['image']
  })

  return hubBlob().put(file.name, file, {
    addRandomSuffix: false,
    prefix: 'images'
  })


})