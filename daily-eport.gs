/*
 * 個人設定
 *
 */
var SLACK_USERNAME = "xxxx";
var SLACK_ICON = ":smile:";
var NAME = "xxxx";
var DEBUG_MAILADDRESS = 'xxxxx';

/**
 * Spreadsheetのカレントシートの日報をSlackへ投稿する
 *
 */
function postDailyReport() {
  var activeSheet = SpreadsheetApp.getActiveSheet();
  var reports = activeSheet.getDataRange().getValues();
  var reportForm = '\
*作業内容*\
\n{0}\
\n\n*問題*\
\n{1}\
\n\n*学び*\
\n{2}\
\n\n*作業予定*\
\n{3}\
\n\nその他**\
\n{4}';
  
  var report = [];
                  
  for (var i = 1; i < reports.length; i++) {    
    for (var j = 0; j < reports[i].length; j++) {
      if (!report[j]) {
        report[j] = [];
      }
      if (reports[i][j]) {
        report[j].push("・ "+reports[i][j]);  
      }
    }
  }
  
  for (var i = 0; i < report.length; i++) {    
    reportForm = reportForm.replace('{'+i+'}', report[i].join("\n"));
  }  
  var body = reportForm;
  
  sendSlack(body);
  
  //デバッグ用(GMAILの下書きに作成されます。)
  //var to = DEBUG_MAILADDRESS;
  //var subject = "日報";
  //GmailApp.createDraft(to, subject, body);  
}

/**
 * Slack投稿関数
 *
 */
function sendSlack(message) {
  var postUrl = 'https://hooks.slack.com/services/xxxxxxxxxx';
  var username = SLACK_USERNAME;
  var icon = SLACK_ICON;
  var message = message;  
  
  var jsonData =
  {
     "username" : username,
     "icon_emoji": icon,
     "text" : message
  };
  var payload = JSON.stringify(jsonData);

  var options =
  {
    "method" : "post",
    "contentType" : "application/json",
    "payload" : payload
  };
  UrlFetchApp.fetch(postUrl, options);
}

/**
 * 月末締めのレポートの出力
 *
 */
function monthlyReport() {
  var FOLDER_ID = 'xxxxxxxxxx';
  var sheets = SpreadsheetApp.getActiveSpreadsheet().getSheets();
  var report = [];
  var dt = new Date();
  
  for (var i = 0; i < sheets.length; i++) {
    var data = [];
    var name = sheets[i].getSheetName();
    var inner = sheets[i].getRange(2, 1, sheets[i].getLastRow() - 1).getValues();    
    var text = [];
    for (var j=0; j < inner.length; j++) {
      if (!inner[j][0]) {
        break;
      }
      text.push('* ' + inner[j][0]);
    }
    report[name] = text;
  }
  var reportForm = '\
<' + NAME + '>\
\
\n\n{DATA}\
';
  var keys = Object.keys(report);
  var text = '';
  for (var i = 0; i < keys.length; i++) {
      text += dt.getFullYear() + "/" + keys[i] + "\n\n";
      text += report[keys[i]].join("\n");
      text += "\n\n"    
  } 
  reportForm = reportForm.replace('{DATA}', text);

  doc = DocumentApp.create(dt.getFullYear() + "_" + (dt.getMonth() + 1) + "_daily-report_" + NAME + ".txt");
  body = doc.getBody().editAsText();
  body.insertText(0, reportForm)
  var file = DriveApp.getFileById(doc.getId());
  var folderTarget = DriveApp.getFolderById(FOLDER_ID);
  folderTarget.addFile(file);
}
/**
 * 月初めコピーしたブックの不要なシート削除する
 *
 */
function removeSheetForNewBook() {
  var bk = SpreadsheetApp.getActiveSpreadsheet();
　 　var arr_sh = bk.getSheets();
  for (var i = 1; i < arr_sh.length; i++) {
    //1つのシートを残して全削除
    bk.deleteSheet(arr_sh[i]);
  }
}
