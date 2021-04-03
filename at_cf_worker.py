async function handleRequest(request) {
  const init = {
    headers: {
      'content-type': 'text/html;charset=UTF-8',
    },
  }

  // 获取workers URL 上的参数
  const selfUrl = request.url;                                 // 获取worker链接
  const getType = getQueryVariable('type',selfUrl).replace(/-/,"_");           // 获取页码参数
  let url = ""
  if (getType && allowName.indexOf(getType) !=-1) {
    url = someHost + getType.replace(/-/,"_") + ".txt"
  } else {
    url = someHost + "AT_best.txt"
  }
  console.log(allowName.indexOf(getType))
  

  const response = await fetch(url, init)
  const results = await gatherResponse(response)
  return new Response(results, init)
}
addEventListener('fetch', event => {
  return event.respondWith(handleRequest(event.request))
})
/**
 * gatherResponse awaits and returns a response body as a string.
 * Use await gatherResponse(..) in an async function to get the response body
 * @param {Response} response
 */
async function gatherResponse(response) {
  const { headers } = response
  const contentType = headers.get('content-type')
  if (contentType.includes('application/json')) {
    return await response.json()
  } else if (contentType.includes('application/text')) {
    return await response.text()
  } else if (contentType.includes('text/html')) {
    return await response.text()
  } else {
    return await response.text()
  }
}

// 获取worker URL上传递的GET参数
function getQueryVariable(variable,url){
    if (url.indexOf("?") != -1) {
        let query = url.split("?")[1]
        let vars = query.split("&");
        for (let i=0;i<vars.length;i++) {
            let pair = vars[i].split("=");
            if(pair[0] == variable){return pair[1];}
        }
    };
    return("");
}

/**
 * Example someHost at url is set up to respond with HTML
 * Replace url with the host you wish to send requests to
 *  */
const allowName = ["AT_best","AT_all","AT_bad","AT_all_udp","AT_all_http","AT_all_https","AT_all_ws","AT_best_ip","AT_all_ip","ATaria2_best","ATaria2_all","ATaria2_bad","ATaria2_all_udp","ATaria2_all_http","ATaria2_all_https","ATaria2_all_ws","ATaria2_best_ip","ATaria2_all_ip"]
const someHost = 'https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/'
