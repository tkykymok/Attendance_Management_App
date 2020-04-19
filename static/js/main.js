const toDoubleDigits = function(num) {
    num += "";
    if (num.length === 1) {
      num = "0" + num;
    }
   return num;     
  };
  // 日付をYYYY/MM/DD HH:DD:MI:SS形式で取得
const yyyymmddhhmiss = function () {
    const date = new Date();
    const yyyy = date.getFullYear();
    const mm = toDoubleDigits(date.getMonth() + 1);
    const dd = toDoubleDigits(date.getDate());
    const hh = toDoubleDigits(date.getHours());
    const mi = toDoubleDigits(date.getMinutes());
    return yyyy + '/' + mm + '/' + dd + ' ' + hh + ':' + mi;
};

const now = yyyymmddhhmiss();

$('#attend').on('click', function () {
    
    alert(`${now} 出勤しました`);
});

$('#leave').on('click', function () {
    alert(`${now} 退勤しました`);
});

