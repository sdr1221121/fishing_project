import 'package:flutter/material.dart';
import 'core/theme/app_theme.dart';
import 'screens/home_screen.dart';
import 'notifications/notification_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await NotificationService.initialize();
  await NotificationService.requestNotificationPermission(); 

  runApp(const PescaApp());
}

class PescaApp extends StatelessWidget {
  const PescaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gestão de Pesca',
      theme: AppTheme.theme,
      home: const HomeWithTestButton(),
      debugShowCheckedModeBanner: false,
    );
  }
}

/// Widget que mantém a HomeScreen original e adiciona botão de teste
class HomeWithTestButton extends StatelessWidget {
  const HomeWithTestButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: const [
          HomeScreen(),
          Align(
            alignment: Alignment.bottomCenter,
            child: Padding(
              padding: EdgeInsets.all(16.0),
              //child: TestNotificationButton(),
            ),
          ),
        ],
      ),
    );
  }
}

class TestNotificationButton extends StatelessWidget {
  const TestNotificationButton({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        NotificationService.showNotification(
          title: 'Teste',
          body: 'Notificação local disparada com sucesso!',
        );
        print("Notificação enviada!");

      },
      child: const Text('Enviar Notificação de Teste'),
    );
  }
}
