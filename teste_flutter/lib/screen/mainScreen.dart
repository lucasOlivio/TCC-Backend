import "package:flutter/material.dart";

class MainScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Flutter Teste TCC"),
        centerTitle: true,
      ),
      body: Container(
        child: Column(
          children: <Widget>[
            Padding(
              padding: EdgeInsets.fromLTRB(0,90,0,70),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Icon(
                    Icons.monetization_on,
                    color: Colors.green,
                    size: 90.0,
                  )
                ],
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Column(
                  children: <Widget>[
                    Padding(
                      padding: EdgeInsets.fromLTRB(25, 0, 25, 5),
                      child: Icon(
                        Icons.pie_chart,
                        color: Colors.green,
                        size: 60.0,
                      ),
                    ),
                    Text("Opção 1")
                  ],
                ),
                Column(
                  children: <Widget>[
                    Padding(
                      padding: EdgeInsets.fromLTRB(25, 0, 25, 5),
                      child: Icon(
                        Icons.insert_chart,
                        color: Colors.green,
                        size: 60.0,
                      ),
                    ),
                    Text("Opção 2")
                  ],
                ), Column(
                  children: <Widget>[
                    Padding(
                      padding: EdgeInsets.fromLTRB(25, 0, 25, 5),
                      child: Icon(
                        Icons.attach_money,
                        color: Colors.green,
                        size: 60.0,
                      ),
                    ),
                    Text("Opção 3")
                  ],
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}