<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content = "IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hai</title>
    </head>
    <body>
        <h1>Hello, Input Data In the Form: Name,Name,GameCount</h1>


        <form name="form" method="post">
        <input type="text" name="Player1" id="Player1" value="">
        <input type="text" name="Player2" id="Player2" value="">
        <input type="text" name="GameCount" id="GameCount" value="">
        <button onclick="run()">Submit</button>
        </form>


        <?php
            $Player1 = $_POST['Player1']; 
            $Player2 = $_POST['Player2']; 
            $GameCount = $_POST['GameCount']; 
            $data = $Player1 . "," . $Player2 . "," . $GameCount . "\n";
            if (!empty($_POST['Player1'])){
            echo "tada";
            file_put_contents("GameList",$data, FILE_APPEND);
        }
        ?>
        <style>
            body {background-color: darkslategray; text-align:center;}
        </style>
    </body>
</html>