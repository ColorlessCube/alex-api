import {makeAutoObservable} from "mobx";
import {http} from "../utils";

class TextStore {
    text = ''

    constructor() {
        makeAutoObservable(this)
    }

    textFormat = async (input) => {
        this.text = (await http.post('/api/text/format', {
            'text': input
        })).data.data
    }

}

export default TextStore