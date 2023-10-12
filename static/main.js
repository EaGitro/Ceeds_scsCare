





//----------------------------

/**
 * 
 * @param {string} url
 * @returns {Object}  
 */
async function fetchVital(url) {
    const vitalJson = await ((await fetch(url)).json());
    console.log(vitalJson)
    // const vitalJson = await(fetch("http://eagitro.pythonanywhere.com/"))
    // console.log(vitalJson)

    return vitalJson

}


async function updateVital() {
    const vitalJson = await fetchVital('http://tnakamura.pythonanywhere.com/vital-data')
    // console.log(vitalJson)   
    // console.log(typeof vitalJson)
    // console.log(vitalJson.data)
    // // const vitalObj = JSON.parse(vitalJson)
    console.log(vitalJson)
    // document.querySelector("#temperature .value").innerText = vitalJson.hoge


    const vitalValueNodes = document.querySelectorAll(".value")

    let cnt = 0
    const dataNameArr = ["BodyTemperature", "HeartRate", "AverageSleepTime", "OxygenPercent"]

    console.log(vitalValueNodes)
    vitalValueNodes.forEach((x) => {
        console.log(x)
        if(cnt < 4){
            x.innerHTML = vitalJson[dataNameArr[cnt]]["value"]
            cnt += 1
        }
    })
    
    



}

const intervalId = setInterval(async () => {
    try {
        await updateVital();
        // 非同期関数の処理が完了したら、ここで追加の処理を行うことができます
    } catch (error) {
        console.error("updateVital関数でエラーが発生しました:", error);
    }
}, 1000);

// この部分でintervalIdをクリアする方法を提供します
// 例：30秒後にsetIntervalを停止する場合
setTimeout(() => {
    clearInterval(intervalId);
}, 30000);



updateVital()




