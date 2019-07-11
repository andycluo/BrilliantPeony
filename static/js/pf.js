var insertText = '<div id="apDiv" style="right:30px; position:fixed; width:180px; height:200px; z-index:2; background-image:url(image/adv.jpg);float:left; bottom: 60px;"><span style="float:right;margin-right:15px;"  onclick="close0();">关闭</span><img src="http://yaoshunmudan.com/public/images/code.jpg"/></div>';
document.write(insertText);
var count;
function move()    {

} 
function close0()  {
    document.getElementById('apDiv').style.display = "none";
}
window.onscroll=move;