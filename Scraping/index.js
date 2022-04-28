/** CONSTANTS */

const API = "https://captcha-solver-flask.herokuapp.com/"
const TESTAPI = "http://127.0.0.1:5000/"
const THRESHOLD = 1
const LABELS = [
    'Bicycle', 'Boat', 'Bridge', 'Bus', 'Car', 'Chimney', 'Crosswalk',
    'Hydrant', 'Motorcycle', 'Mountain', 'Palm', 'Stairs', 'Taxi',
    'TowTruck', 'TrafficLight', 'TrafficSign', 'Truck'
]

const QUESTION_MARK = "❓"
const CHECK_MARK = "✔️"
const CROSS_MARK = "❌"
const ERROR_MARK = "⚠️"

/** Radio Listeners */
let imageType = "Truck"
LABELS.forEach((label) => {
    document.querySelector(`#${label}`).addEventListener('click', (event) => {
        imageType = document.querySelector(`label[for='${event.target.id}']`).innerHTML
    })
})

/** TextArea Listener */
document.querySelector("#captcha-link").addEventListener('focusin', (event) => {
    let label = document.querySelector(`label[for='${event.target.id}']`)
    label.innerHTML = "Copy and Paste reCAPTCHA Image Link Here!"
    label.className = "text-light"
    let images = [0, 1, 2, 3, 4, 5, 6, 7, 8].map((val) => document.querySelector(`#image-${val}`).firstChild)
    images.forEach((node) => node.innerHTML = QUESTION_MARK)
})

/** Solve Listener */
document.querySelector("#fetch-test-data").addEventListener('click', async () => {

    /** DOM */
    let label = document.querySelector("label[for='captcha-link']")
    let images = [0, 1, 2, 3, 4, 5, 6, 7, 8].map((val) => document.querySelector(`#image-${val}`).firstChild)
    let spinner = document.querySelector("#spinner")
    spinner.classList.remove("d-none")

    let link = document.querySelector("#captcha-link").value
    if (!link.includes("https://www.google.com/recaptcha/api2/payload?p")) {
        images.forEach((node) => node.innerHTML = ERROR_MARK)
        label.innerHTML = "ERROR: Link not entered correctly"
        label.className = "text-warning"
    } else {
        /** PROCESS INFORMATION  */
        let split = link.split("https://www.google.com/recaptcha/api2/payload?p=")
        let payload = split[split.length-1].replace(/\s+/g, '');

        // const response = await fetch(API + "test/bicycle")
        const response = await fetch(API + `process/${payload}`)
        const data = await response.json()

        if (data["response"] == 200) {
            // success
            let predictions = Array.from([0, 1, 2, 3, 4, 5, 6, 7, 8]).map((val) => {
                return parseFloat(data[`image_${val}`][imageType])
            })
            console.log(predictions)
            let boolArray = predictions.map((val) => val >= THRESHOLD ? true : false)
            images.map((node, index) => {
                if (boolArray[index]) {
                    node.innerHTML = CHECK_MARK
                } else {
                    node.innerHTML = CROSS_MARK
                }
            })
        } else if (data["response"] == 404) {
            // error - can't load image
            images.forEach((node) => node.innerHTML = ERROR_MARK)
            label.innerHTML = "ERROR: Can't access site at provided link"
            label.className = "text-warning"
        } else {
            // error - bad user input
            images.forEach((node) => node.innerHTML = ERROR_MARK)
            label.innerHTML = "ERROR: Something has gone wrong. Try Again!"
            label.className = "text-warning"
        }
    }

    /** CLEANUP */
    spinner.classList.add("d-none")

})
