import "dart:async";
import "package:http/http.dart" as http;
import "dart:convert"; //Conversão de JSON

class User{
  String email;
  String password;

  User(this.email,this.password);

  Future<bool> validateLogin() async{ //Ajustar conexão com API
    bool retornoLogin = await http.get("https://my-json-server.typicode.com/typicode/demo/comments").then((response){
      if(response.statusCode != 200){
        print("Response status: ${response.statusCode}");
        throw(response.statusCode);
      }else{
        return true;
      }
    });
    return retornoLogin;
  }
}