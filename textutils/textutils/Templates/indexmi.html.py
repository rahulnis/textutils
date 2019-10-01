<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Utils</title>
</head>
<body>
<h1>Welcome to the text analyzer. Enter your text below</h1>
<form action='/analyze' method='get'>
    <textarea name='text' style='margin: 0px; width: 721px; height: 93px;'></textarea><br>

    <input type="checkbox" name="removepunc"> Remove Punctuations<br>
      <input type="checkbox" name="fullcaps"> full letter caps<br>
    <input type="checkbox" name="newlineremover"> New Line Remover<br>
    <input type="checkbox" name="extraspaceremover"> Extra Spaces Remover<br>
<input type="checkbox" name="charcount">Character Count<br><br>

    <button type='submit'> Analyze Text</button>

</form>