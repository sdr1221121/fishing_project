class Document {
  final int id;
  final String documentType;
  final DateTime? endDay;
  final String filePath;
  final DateTime? createDate;

  Document({
    required this.id,
    required this.documentType,
    required this.endDay,
    required this.filePath,
    this.createDate,
  });

  factory Document.fromJson(Map<String, dynamic> json) {
  return Document(
    id: json['id'] ?? 0,
    documentType: json['document_type'] ?? '',
    endDay: json['end_day'] != null ? DateTime.tryParse(json['end_day']) : null,
    filePath: json['file_path'] ?? '',
    createDate: json['create_date'] != null ? DateTime.tryParse(json['create_date']) : null,
  );
}


  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'document_type': documentType,
      'end_day': endDay?.toIso8601String(),
      'file_path': filePath,
      'create_date': createDate?.toIso8601String(),
    };
  }
}