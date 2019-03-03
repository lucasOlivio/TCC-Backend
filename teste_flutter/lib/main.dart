import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Teste',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: HomePage(title: 'Flutter Teste TCC'),
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
    return new Column(
        children: <Widget>[
          TextFormField(
            decoration: InputDecoration(
                labelText: 'E-mail'
            ),
            keyboardType: TextInputType.emailAddress,
            validator: (String arg) {
              if((arg.length == 0) || !(arg.contains('@'))) {
                return 'Digite um e-mail válido';
              }else {
                return null;
              }
            },
            onSaved: (String val) {
              _email = val;
            },
          ),

          TextFormField(
            decoration: InputDecoration(
                labelText: 'Senha'
            ),
            obscureText: true,
            validator: (String arg) {
              if(arg.length < 6) {
                return 'Digite uma senha válida';
              }else{
                return null;
              }
            },
            onSaved: (String val) {
              _password = val;
            },
          ),

          RaisedButton(
            child: const Text('Entrar', semanticsLabel: 'Entrar'),
            color: Colors.lightGreen,
            splashColor: Colors.blueGrey,
            onPressed: _validarLogin,
          ),
    ]);
  }

  void _validarLogin(){
    if (_formKey.currentState.validate()) {
      _formKey.currentState.save();
    }else{
      setState(() {
        _autoValidate = true;
      });
    }

    print("Login : $_email e senha: $_password");
    //Inserir função de login
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
            new Form(
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