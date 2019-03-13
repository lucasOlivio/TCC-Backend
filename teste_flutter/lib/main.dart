import "package:flutter/material.dart";
import "package:teste_flutter/class/user.dart";
import "package:teste_flutter/function/widgetGenerator.dart";
import "package:teste_flutter/screen/mainScreen.dart";

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Flutter Teste",
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: HomePage(title: "Flutter Teste TCC"),
    );
  }
}

class HomePage extends StatefulWidget {
  HomePage({Key key, this.title}) : super(key: key);

  final String title;
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  bool _autoValidate = false; //Validação automática ativada caso form. incorreto
  String _email;
  String _password;

  Widget formLogin(){
    return Column(
        children: <Widget>[
          TextFormField(
            decoration: InputDecoration(
                labelText: "E-mail"
            ),
            keyboardType: TextInputType.emailAddress,
            validator: (String arg) {
              Pattern pattern =  r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
              RegExp regex = RegExp(pattern);
              if((arg.length == 0) || !regex.hasMatch(arg)){
                return "Digite um e-mail válido";
              }else{
                return null;
              }
            },
            onSaved: (String val) {
              _email = val;
            },
          ),

          TextFormField(
            decoration: InputDecoration(
                labelText: "Senha"
            ),
            obscureText: true,
            validator: (String arg) {
              if(arg.length < 6) {
                return "Digite uma senha válida";
              }else{
                return null;
              }
            },
            onSaved: (String val) {
              _password = val;
            },
          ),

          RaisedButton(
            child: Text("Entrar", semanticsLabel: "Entrar"),
            color: Colors.lightGreen,
            splashColor: Colors.blueGrey,
            onPressed: _validarLogin,
          ),
    ]);
  }

  void _validarLogin() async {
    bool _loginOK = true;
    if (_formKey.currentState.validate()) {
      _formKey.currentState.save();
    }else{
      _loginOK = false;
      setState(() {
        _autoValidate = true;
      });
    }

    if(_loginOK){
      User user = new User(_email,_password);
      try{
        if(await user.validateLogin()){
          print("Usuário logado!");
          Navigator.pushReplacement(context,MaterialPageRoute(builder: (context) => MainScreen()));
        }else{
          print("Usuário não encontrado!");
          buildAlert(context,"Usuário não encontrado!","Email/Senha incorretos");
        }
      }catch(e){
        print(e.toString());
        buildAlert(context,"Ocorreu um erro!","Tente novamente em instantes");
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.only(top:0),
              child: Icon(
                Icons.monetization_on,
                color:  Colors.green,
                size: 90.0,
              ), 
            ),
            Form(
              key: _formKey,
              autovalidate: _autoValidate,
              child: formLogin(),
            ),
          ],
        ),
      ),
    );
  }
}