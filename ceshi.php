<?php
/*************************************************************************
> File Name: ceshi.php
> Author: arkulo
> Mail: arkulo@163.com 
> Created Time: 2013年09月20日 星期五 21时06分34秒
*************************************************************************/

$con = mysql_connect("localhost:3307","root","") or die("error casue by connect mysql");
mysql_select_db("mydb",$con);
mysql_query("set names utf8");

$sqlOne = "select title from a_img_lib where id=8";
$r = mysql_query($sqlOne);
$res = mysql_fetch_assoc($r);
echo $res['title'],"\n";


$ch = curl_init();
$search = urlencode($res['title']);
curl_setopt($ch,CURLOPT_URL,"http://translate.google.com.hk/translate_a/t?client=t&sl=en&tl=zh-CN&hl=zh-CN&sc=2&ie=UTF-8&oe=UTF-8&pc=1&oc=1&otf=1&ssel=0&tsel=0&q=$search");
curl_setopt($ch,CURLOPT_HEADER,false);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
$result=curl_exec($ch);
curl_close($ch);
//print $result;exit;


$regex = "/\".*?\"/";
$matches = array();
if(preg_match_all($regex,$result,$matches))
{
    echo $matches[0][0],"\n";
}else
{
    echo "no\n";
}
