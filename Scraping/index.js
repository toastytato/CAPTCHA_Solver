const API = "https://captcha-solver-flask.herokuapp.com/"  

document.querySelector("#fetch-test-data").addEventListener('click', async() => {
    console.log("getting data")
    const response = await fetch(API + "test/bicycle")
    const data = await response.json()
    console.log(data)
})

// const fetchTestData = async () => {
//     console.log("getting data")
//     const response = await fetch(API + "test/bicycle")
//     const data = await response.json()
//     console.log(data)
// }