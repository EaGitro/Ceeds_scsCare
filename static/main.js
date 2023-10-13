//----------------------------

/**
 *
 * @param {string} url
 * @returns {Object}
 */
async function fetchVital(url) {
  const vitalJson = await (await fetch(url)).json();
  console.log(vitalJson);
  // const vitalJson = await(fetch("http://eagitro.pythonanywhere.com/"))
  // console.log(vitalJson)

  return vitalJson;
}

async function updateVital() {
  const vitalJson = await fetchVital(
    "http://tnakamura.pythonanywhere.com/vital-data"
  );
  // console.log(vitalJson)
  // console.log(typeof vitalJson)
  // console.log(vitalJson.data)
  // // const vitalObj = JSON.parse(vitalJson)
  console.log(vitalJson);
  // document.querySelector("#temperature .value").innerText = vitalJson.hoge

  const vitalValueNodes = document.querySelectorAll(".value");
  const heartImgNodes = document.querySelectorAll(".heart");

  let vitalCnt = 0;
  let heartCnt = 0;
  const dataNameArr = [
    "BodyTemperature",
    "HeartRate",
    "AverageSleepTime",
    "OxygenPercent",
  ];

  console.log(vitalValueNodes);
  vitalValueNodes.forEach((x) => {
    console.log(x);
    if (vitalCnt < 4) {
      x.innerHTML = vitalJson[dataNameArr[vitalCnt]]["value"];
      vitalCnt += 1;
    }
  });

  heartImgNodes.forEach((x) => {
    console.log(x);
    if (heartCnt < 4) {
      if (vitalJson[dataNameArr[heartCnt]]["bool"]) {
        x.innerHTML = `<svg width="18" height="16" viewBox="0 0 18 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <ellipse cx="5.08696" cy="4.05952" rx="4.30435" ry="4.05952" fill="#FC6565"/>
                            <ellipse cx="12.913" cy="4.05952" rx="4.30435" ry="4.05952" fill="#FC6565"/>
                            <path d="M9 15.5L1.20577 6.08929L16.7942 6.08929L9 15.5Z" fill="#FC6565"/>
                        </svg>`;
      } else {
        x.innerHTML = `
        <svg width="26" height="24" viewBox="0 0 26 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g filter="url(#filter0_d_2_24)">
            <ellipse cx="9.08696" cy="4.05952" rx="4.30435" ry="4.05952" fill="#D9D9D9"/>
            <ellipse cx="16.913" cy="4.05952" rx="4.30435" ry="4.05952" fill="#D9D9D9"/>
            <path d="M13 15.5L5.20577 6.08929L20.7942 6.08929L13 15.5Z" fill="#D9D9D9"/>
            </g>
            <defs>
            <filter id="filter0_d_2_24" x="0.782608" y="0" width="24.4348" height="23.5" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
            <feOffset dy="4"/>
            <feGaussianBlur stdDeviation="2"/>
            <feComposite in2="hardAlpha" operator="out"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_2_24"/>
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_2_24" result="shape"/>
            </filter>
            </defs>
        </svg>
        `;
      }

      heartCnt += 1;
    }
  });
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

updateVital();
