
const axios = require("axios")
const url = 'https://constable-github.firebaseio.com'

async function grade_update(_path, grade){
    const body = {"grade": grade}
    const response = await axios.put(`${url}/${_path}.json`, body, {
        headers: {
            "Content-type": "application/json",
        }
    })
    return response
}

module.exports = {
    update
}