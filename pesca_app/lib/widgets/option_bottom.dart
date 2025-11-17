import 'package:flutter/material.dart';

class OptionItem {
  final IconData icon;
  final String label;
  final VoidCallback onTap;

  OptionItem({required this.icon, required this.label, required this.onTap});
}

void showOptions({
  required BuildContext context,
  required String title,
  required List<OptionItem> options,
}) {
  showModalBottomSheet(
    context: context,
    builder: (context) {
      return SafeArea(
        child: Wrap(
          children: [
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text(
                title,
                style: const TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            for (final option in options)
              ListTile(
                leading: Icon(option.icon),
                title: Text(option.label),
                onTap: () {
                  Navigator.of(context).pop();
                  option.onTap();
                },
              ),
          ],
        ),
      );
    },
  );
}
