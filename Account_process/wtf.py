import requests

url = "http://dev.comment-bot.teky.edu.vn/admin/botComment/accounts/"

payload = 'csrfmiddlewaretoken=seNH7GG9FBLk99oMDNJ3JefSsnaZNLMJ0HusisEGTXfhCQEXJxrBHCoSWV6GgKBj&action=delete_selected&select_across=0&index=0&post=yes'
payload += '_selected_action=59261&_selected_action=59260&_selected_action=59259&_selected_action=59258&_selected_action=59257&_selected_action=59256&_selected_action=59255&_selected_action=59254&_selected_action=59253&_selected_action=59252&_selected_action=59251&_selected_action=59250&_selected_action=59249&_selected_action=59248&_selected_action=59247&_selected_action=59246&_selected_action=59245&_selected_action=59244&_selected_action=59243&_selected_action=59242&_selected_action=59241&_selected_action=59240&_selected_action=59239&_selected_action=59238&_selected_action=59237&_selected_action=59236&_selected_action=59235&_selected_action=59234&_selected_action=59233&_selected_action=59232&_selected_action=59231&_selected_action=59230&_selected_action=59229&_selected_action=59228&_selected_action=59227&_selected_action=59226&_selected_action=59225&_selected_action=59224&_selected_action=59223&_selected_action=59222&_selected_action=59221&_selected_action=59220&_selected_action=59219&_selected_action=59218&_selected_action=59217&_selected_action=59216&_selected_action=59215&_selected_action=59214&_selected_action=59213&_selected_action=59212&_selected_action=59211&_selected_action=59210&_selected_action=59209&_selected_action=59208&_selected_action=59207&_selected_action=59206&_selected_action=59205&_selected_action=59204&_selected_action=59203&_selected_action=59202&_selected_action=59201&_selected_action=59200&_selected_action=59199&_selected_action=59198&_selected_action=59197&_selected_action=59196&_selected_action=59195&_selected_action=59194&_selected_action=59193&_selected_action=59192&_selected_action=59191&_selected_action=59190&_selected_action=59189&_selected_action=59188&_selected_action=59187&_selected_action=59186&_selected_action=59185&_selected_action=59184&_selected_action=59183&_selected_action=59182&_selected_action=59181&_selected_action=59180&_selected_action=59179&_selected_action=59178&_selected_action=59177&_selected_action=59176&_selected_action=59175&_selected_action=59174&_selected_action=59173&_selected_action=59172&_selected_action=59171&_selected_action=59170&_selected_action=59169&_selected_action=59168&_selected_action=59167&_selected_action=59166&_selected_action=59165&_selected_action=59164&_selected_action=59163&_selected_action=59162&_selected_action=59161&_selected_action=59160&_selected_action=59159&_selected_action=59158&_selected_action=59157&_selected_action=59156&_selected_action=59155&_selected_action=59154&_selected_action=59153&_selected_action=59152&_selected_action=59151&_selected_action=59150&_selected_action=59149&_selected_action=59148&_selected_action=59147&_selected_action=59146&_selected_action=59145&_selected_action=59144&_selected_action=59143&_selected_action=59142&_selected_action=59141&_selected_action=59140&_selected_action=59139&_selected_action=59138&_selected_action=59137&_selected_action=59136&_selected_action=59135&_selected_action=59134&_selected_action=59133&_selected_action=59132&_selected_action=59131&_selected_action=59130&_selected_action=59129&_selected_action=59128&_selected_action=59127&_selected_action=59126&_selected_action=59125&_selected_action=59124&_selected_action=59123&_selected_action=59122&_selected_action=59121&_selected_action=59120&_selected_action=59119&_selected_action=59118&_selected_action=59117&_selected_action=59116&_selected_action=59115&_selected_action=59114&_selected_action=59113&_selected_action=59112&_selected_action=59111&_selected_action=59110&_selected_action=59109&_selected_action=59108&_selected_action=59107&_selected_action=59106&_selected_action=59105&_selected_action=59104&_selected_action=59103&_selected_action=59102&_selected_action=59101&_selected_action=59100&_selected_action=59099&_selected_action=59098&_selected_action=59097&_selected_action=59096&_selected_action=59095&_selected_action=59094&_selected_action=59093&_selected_action=59092&_selected_action=59091&_selected_action=59090&_selected_action=59089&_selected_action=59088&_selected_action=59087&_selected_action=59086&_selected_action=59085&_selected_action=59084&_selected_action=59083&_selected_action=59082&_selected_action=59081&_selected_action=59080&_selected_action=59079&_selected_action=59078&_selected_action=59077&_selected_action=59076&_selected_action=59075&_selected_action=59074&_selected_action=59073&_selected_action=59072&_selected_action=59071&_selected_action=59070&_selected_action=59069&_selected_action=59068&_selected_action=59067&_selected_action=59066&_selected_action=59065&_selected_action=59064&_selected_action=59063&_selected_action=59062&_selected_action=59061&_selected_action=59060&_selected_action=59059&_selected_action=59058&_selected_action=59057&_selected_action=59056&_selected_action=59055&_selected_action=59054&_selected_action=59053&_selected_action=59052&_selected_action=59051&_selected_action=59050&_selected_action=59049&_selected_action=59048&_selected_action=59047&_selected_action=59046&_selected_action=59045&_selected_action=59044&_selected_action=59043&_selected_action=59042&_selected_action=59041&_selected_action=59040&_selected_action=59039&_selected_action=59038&_selected_action=59037&_selected_action=59036&_selected_action=59035&_selected_action=59034&_selected_action=59033&_selected_action=59032&_selected_action=59031&_selected_action=59030&_selected_action=59029&_selected_action=59028&_selected_action=59027&_selected_action=59026&_selected_action=59025&_selected_action=59024&_selected_action=59023&_selected_action=59022&_selected_action=59021&_selected_action=59020&_selected_action=59019&_selected_action=59018&_selected_action=59017&_selected_action=59016&_selected_action=59015&_selected_action=59014&_selected_action=59013&_selected_action=59012&_selected_action=59011&_selected_action=59010&_selected_action=59009&_selected_action=59008&_selected_action=59007&_selected_action=59006&_selected_action=59005&_selected_action=59004&_selected_action=59003&_selected_action=59002&_selected_action=59001&_selected_action=59000&_selected_action=58999&_selected_action=58998&_selected_action=58997&_selected_action=58996&_selected_action=58995&_selected_action=58994&_selected_action=58993&_selected_action=58992&_selected_action=58991&_selected_action=58990&_selected_action=58989&_selected_action=58988&_selected_action=58987&_selected_action=58986&_selected_action=58985&_selected_action=58984&_selected_action=58983&_selected_action=58982&_selected_action=58981&_selected_action=58980&_selected_action=58979&_selected_action=58978&_selected_action=58977&_selected_action=58976&_selected_action=58975&_selected_action=58974&_selected_action=58973&_selected_action=58972&_selected_action=58971&_selected_action=58970&_selected_action=58969&_selected_action=58968&_selected_action=58967&_selected_action=58966&_selected_action=58965&_selected_action=58964&_selected_action=58963&_selected_action=58962&_selected_action=58961&_selected_action=58960&_selected_action=58959&_selected_action=58958&_selected_action=58957&_selected_action=58956&_selected_action=58955&_selected_action=58954&_selected_action=58953&_selected_action=58952&_selected_action=58951&_selected_action=58950&_selected_action=58949&_selected_action=58948&_selected_action=58947&_selected_action=58946&_selected_action=58945&_selected_action=58944&_selected_action=58943&_selected_action=58942&_selected_action=58941&_selected_action=58940&_selected_action=58939&_selected_action=58938&_selected_action=58937&_selected_action=58936&_selected_action=58935&_selected_action=58934&_selected_action=58933&_selected_action=58932&_selected_action=58931&_selected_action=58930&_selected_action=58929&_selected_action=58928&_selected_action=58927&_selected_action=58926&_selected_action=58925&_selected_action=58924&_selected_action=58923&_selected_action=58922&_selected_action=58921&_selected_action=58920&_selected_action=58919&_selected_action=58918&_selected_action=58917&_selected_action=58916&_selected_action=58915&_selected_action=58914&_selected_action=58913&_selected_action=58912&_selected_action=58911&_selected_action=58910&_selected_action=58909&_selected_action=58908&_selected_action=58907&_selected_action=58906&_selected_action=58905&_selected_action=58904&_selected_action=58903&_selected_action=58902&_selected_action=58901&_selected_action=58900&_selected_action=58899&_selected_action=58898&_selected_action=58897&_selected_action=58896&_selected_action=58895&_selected_action=58894&_selected_action=58893&_selected_action=58892&_selected_action=58891&_selected_action=58890&_selected_action=58889&_selected_action=58888&_selected_action=58887&_selected_action=58886&_selected_action=58885&_selected_action=58884&_selected_action=58883&_selected_action=58882&_selected_action=58881&_selected_action=58880&_selected_action=58879&_selected_action=58878&_selected_action=58877&_selected_action=58876&_selected_action=58875&_selected_action=58874&_selected_action=58873&_selected_action=58872&_selected_action=58871&_selected_action=58870&_selected_action=58869&_selected_action=58868&_selected_action=58867&_selected_action=58866&_selected_action=58865&_selected_action=58864&_selected_action=58863&_selected_action=58862&_selected_action=58861&_selected_action=58860&_selected_action=58859&_selected_action=58858&_selected_action=58857&_selected_action=58856&_selected_action=58855&_selected_action=58854&_selected_action=58853&_selected_action=58852&_selected_action=58851&_selected_action=58850&_selected_action=58849&_selected_action=58848&_selected_action=58847&_selected_action=58846&_selected_action=58845&_selected_action=58844&_selected_action=58843&_selected_action=58842&_selected_action=58841&_selected_action=58840&_selected_action=58839&_selected_action=58838&_selected_action=58837&_selected_action=58836&_selected_action=58835&_selected_action=58834&_selected_action=58833&_selected_action=58832&_selected_action=58831&_selected_action=58830&_selected_action=58829&_selected_action=58828&_selected_action=58827&_selected_action=58826&_selected_action=58825&_selected_action=58824&_selected_action=58823&_selected_action=58822&_selected_action=58821&_selected_action=58820&_selected_action=58819&_selected_action=58818&_selected_action=58817&_selected_action=58816&_selected_action=58815&_selected_action=58814&_selected_action=58813&_selected_action=58812&_selected_action=58811&_selected_action=58810&_selected_action=58809&_selected_action=58808&_selected_action=58807&_selected_action=58806&_selected_action=58805&_selected_action=58804&_selected_action=58803&_selected_action=58802&_selected_action=58801&_selected_action=58800&_selected_action=58799&_selected_action=58798&_selected_action=58797&_selected_action=58796&_selected_action=58795&_selected_action=58794&_selected_action=58793&_selected_action=58792&_selected_action=58791&_selected_action=58790&_selected_action=58789&_selected_action=58788&_selected_action=58787&_selected_action=58786&_selected_action=58785&_selected_action=58784&_selected_action=58783&_selected_action=58782&_selected_action=58781&_selected_action=58780&_selected_action=58779&_selected_action=58778&_selected_action=58777&_selected_action=58776&_selected_action=58775&_selected_action=58774&_selected_action=58773&_selected_action=58772&_selected_action=58771&_selected_action=58770&_selected_action=58769&_selected_action=58768&_selected_action=58767&_selected_action=58766&_selected_action=58765&_selected_action=58764&_selected_action=58763&_selected_action=58762&_selected_action=58761&_selected_action=58760&_selected_action=58759&_selected_action=58758&_selected_action=58757&_selected_action=58756&_selected_action=58755&_selected_action=58754&_selected_action=58753&_selected_action=58752&_selected_action=58751&_selected_action=58750&_selected_action=58749&_selected_action=58748&_selected_action=58747&_selected_action=58746&_selected_action=58745&_selected_action=58744&_selected_action=58743&_selected_action=58742&_selected_action=58741&_selected_action=58740&_selected_action=58739&_selected_action=58738&_selected_action=58737&_selected_action=58736&_selected_action=58735&_selected_action=58734&_selected_action=58733&_selected_action=58732&_selected_action=58731&_selected_action=58730&_selected_action=58729&_selected_action=58728&_selected_action=58727&_selected_action=58726&_selected_action=58725&_selected_action=58724&_selected_action=58723&_selected_action=58722&_selected_action=58721&_selected_action=58720&_selected_action=58719&_selected_action=58718&_selected_action=58717&_selected_action=58716&_selected_action=58715&_selected_action=58714&_selected_action=58713&_selected_action=58712&_selected_action=58711&_selected_action=58710&_selected_action=58709&_selected_action=58708&_selected_action=58707&_selected_action=58706&_selected_action=58705&_selected_action=58704&_selected_action=58703&_selected_action=58702&_selected_action=58701&_selected_action=58700&_selected_action=58699&_selected_action=58698&_selected_action=58697&_selected_action=58696&_selected_action=58695&_selected_action=58694&_selected_action=58693&_selected_action=58692&_selected_action=58691&_selected_action=58690&_selected_action=58689&_selected_action=58688&_selected_action=58687&_selected_action=58686&_selected_action=58685&_selected_action=58684&_selected_action=58683&_selected_action=58682&_selected_action=58681&_selected_action=58680&_selected_action=58679&_selected_action=58678&_selected_action=58677&_selected_action=58676&_selected_action=58675&_selected_action=58674&_selected_action=58673&_selected_action=58672&_selected_action=58671&_selected_action=58670&_selected_action=58669&_selected_action=58668&_selected_action=58667&_selected_action=58666&_selected_action=58665&_selected_action=58664&_selected_action=58663&_selected_action=58662&_selected_action=58661&_selected_action=58660&_selected_action=58659&_selected_action=58658&_selected_action=58657&_selected_action=58656&_selected_action=58655&_selected_action=58654&_selected_action=58653&_selected_action=58652&_selected_action=58651&_selected_action=58650&_selected_action=58649&_selected_action=58648&_selected_action=58647&_selected_action=58646&_selected_action=58645&_selected_action=58644&_selected_action=58643&_selected_action=58642&_selected_action=58641&_selected_action=58640&_selected_action=58639&_selected_action=58638&_selected_action=58637&_selected_action=58636&_selected_action=58635&_selected_action=58634&_selected_action=58633&_selected_action=58632&_selected_action=58631&_selected_action=58630&_selected_action=58629&_selected_action=58628&_selected_action=58627&_selected_action=58626&_selected_action=58625&_selected_action=58624&_selected_action=58623&_selected_action=58622&_selected_action=58621&_selected_action=58620&_selected_action=58619&_selected_action=58618&_selected_action=58617&_selected_action=58616&_selected_action=58615&_selected_action=58614&_selected_action=58613&_selected_action=58612&_selected_action=58611&_selected_action=58610&_selected_action=58609&_selected_action=58608&_selected_action=58607&_selected_action=58606&_selected_action=58605&_selected_action=58604&_selected_action=58603&_selected_action=58602&_selected_action=58601&_selected_action=58600&_selected_action=58599&_selected_action=58598&_selected_action=58597&_selected_action=58596&_selected_action=58595&_selected_action=58594&_selected_action=58593&_selected_action=58592&_selected_action=58591&_selected_action=58590&_selected_action=58589&_selected_action=58588&_selected_action=58587&_selected_action=58586&_selected_action=58585&_selected_action=58584&_selected_action=58583&_selected_action=58582&_selected_action=58581&_selected_action=58580&_selected_action=58579&_selected_action=58578&_selected_action=58577&_selected_action=58576&_selected_action=58575&_selected_action=58574&_selected_action=58573&_selected_action=58572&_selected_action=58571&_selected_action=58570&_selected_action=58569&_selected_action=58568&_selected_action=58567&_selected_action=58566&_selected_action=58565&_selected_action=58564&_selected_action=58563&_selected_action=58562&_selected_action=58561&_selected_action=58560&_selected_action=58559&_selected_action=58558&_selected_action=58557&_selected_action=58556&_selected_action=58555&_selected_action=58554&_selected_action=58553&_selected_action=58552&_selected_action=58551&_selected_action=58550&_selected_action=58549&_selected_action=58548&_selected_action=58547&_selected_action=58546&_selected_action=58545&_selected_action=58544&_selected_action=58543&_selected_action=58542&_selected_action=58541&_selected_action=58540&_selected_action=58539&_selected_action=58538&_selected_action=58537&_selected_action=58536&_selected_action=58535&_selected_action=58534&_selected_action=58533&_selected_action=58532&_selected_action=58531&_selected_action=58530&_selected_action=58529&_selected_action=58528&_selected_action=58527&_selected_action=58526&_selected_action=58525&_selected_action=58524&_selected_action=58523&_selected_action=58522&_selected_action=58521&_selected_action=58520&_selected_action=58519&_selected_action=58518&_selected_action=58517&_selected_action=58516&_selected_action=58515&_selected_action=58514&_selected_action=58513&_selected_action=58512&_selected_action=58511&_selected_action=58510&_selected_action=58509&_selected_action=58508&_selected_action=58507&_selected_action=58506&_selected_action=58505&_selected_action=58504&_selected_action=58503&_selected_action=58502&_selected_action=58501&_selected_action=58500&_selected_action=58499&_selected_action=58498&_selected_action=58497&_selected_action=58496&_selected_action=58495&_selected_action=58494&_selected_action=58493&_selected_action=58492&_selected_action=58491&_selected_action=58490&_selected_action=58489&_selected_action=58488&_selected_action=58487&_selected_action=58486&_selected_action=58485&_selected_action=58484&_selected_action=58483&_selected_action=58482&_selected_action=58481&_selected_action=58480&_selected_action=58479&_selected_action=58478&_selected_action=58477&_selected_action=58476&_selected_action=58475&_selected_action=58474&_selected_action=58473&_selected_action=58472&_selected_action=58471&_selected_action=58470&_selected_action=58469&_selected_action=58468&_selected_action=58467&_selected_action=58466&_selected_action=58465&_selected_action=58464&_selected_action=58463&_selected_action=58462&_selected_action=58461&_selected_action=58460&_selected_action=58459&_selected_action=58458&_selected_action=58457&_selected_action=58456&_selected_action=58455&_selected_action=58454&_selected_action=58453&_selected_action=58452&_selected_action=58451&_selected_action=58450&_selected_action=58449&_selected_action=58448&_selected_action=58447&_selected_action=58446&_selected_action=58445&_selected_action=58444&_selected_action=58443&_selected_action=58442&_selected_action=58441&_selected_action=58440&_selected_action=58439&_selected_action=58438&_selected_action=58437&_selected_action=58436&_selected_action=58435&_selected_action=58434&_selected_action=58433&_selected_action=58432&_selected_action=58431&_selected_action=58430&_selected_action=58429&_selected_action=58428&_selected_action=58427&_selected_action=58426&_selected_action=58425&_selected_action=58424&_selected_action=58423&_selected_action=58422&_selected_action=58421&_selected_action=58420&_selected_action=58419&_selected_action=58418&_selected_action=58417&_selected_action=58416&_selected_action=58415&_selected_action=58414&_selected_action=58413&_selected_action=58412&_selected_action=58411&_selected_action=58410&_selected_action=58409&_selected_action=58408&_selected_action=58407&_selected_action=58406&_selected_action=58405&_selected_action=58404&_selected_action=58403&_selected_action=58402&_selected_action=58401&_selected_action=58400&_selected_action=58399&_selected_action=58398&_selected_action=58397&_selected_action=58396&_selected_action=58395&_selected_action=58394&_selected_action=58393&_selected_action=58392&_selected_action=58391&_selected_action=58390&_selected_action=58389&_selected_action=58388&_selected_action=58387&_selected_action=58386&_selected_action=58385&_selected_action=58384&_selected_action=58383&_selected_action=58382'
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'en,en-US;q=0.9,vi;q=0.8',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'DNT': '1',
  'Origin': 'http://dev.comment-bot.teky.edu.vn',
  'Referer': 'http://dev.comment-bot.teky.edu.vn/admin/botComment/accounts/',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

# login to the website then delete the accounts
with requests.Session() as s:
 login_payload = 'csrfmiddlewaretoken=jmYqFkfkClT1DF32vUFCtmbYQvnDcqpARPFbQ6dRQHnY6mjdBEnarKkYk3jkFpea&username=admin&password=matkhau123%40&next=%2Fadmin%2F'
 login_response = s.post('http://dev.comment-bot.teky.edu.vn/admin/login/?next=/admin/', data=login_payload, headers=headers)
 response = s.post(url, headers=headers, data=payload)
 print(response.text)