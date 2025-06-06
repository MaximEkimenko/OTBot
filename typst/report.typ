
        // базовые настройки
        #set page(
                width: 210mm,
                height: 297mm,
                margin: 0.2cm
                )
        //#set text(font: "Arial", size: 10pt)        
        #set text(
            font: (
                "Liberation Sans",  // Основной шрифт для Linux
                "Noto Sans",        // Fallback 1
                "DejaVu Sans",      // Fallback 2
                "Arial",            // Fallback 3 (если вдруг есть)
            ),
            size: 10pt
            )        
        #set heading(numbering: "1.")

        // стили
        #let centered-title(body) = align(center)[
            #text(size: 16pt, weight: "bold")[#body]]

        // шапка
        #align(right)[Ответственным: \ Новый.]
        #align(right)[Копия: главному инженеру \ Новиков А.Н..]
        #align(right)[от РуководительООТПБиООС \
        Максим]

        // заголовок
        #centered-title[Предписание]
        Дата формирования предписания: 06.06.2025
        #centered-title[Устранить следующие нарушения:]

        // таблица
        #set table(
            align: center,
            inset: 5pt,
            stroke: 0.5pt
            )
        #table(
            columns: (
                1.2cm,
                2cm, 
                auto,
                5.2cm,
                4cm,
                2.2cm,
                    ),
            // шапка таблицы
            [*№ п/п*],
            [*Дата*],
            [*Фото выявленных нарушений*],
            [*Перечень выявленных нарушений*],
            [*Сроки устранения. Мероприятия*],
            [*Факт устранения*],
        
            [28],
            //[06.06.2025 12:24],
            [06.06.2025 12:24],
            image("violation_images\violation_1.jpg", width: auto),
            [#align(left)[
            Описание: Без описания \ \
            Категория: Отсутствует/имеет повреждения обозначения газопровода \ \
            Место нарушения: Производственный цех №1 \ \
            Ответственный: Новый \ \
            Нарушение зафиксировал: Максим]],
            [#align(left)[Усилить контроль за выполнением работ. Срок устранения: Немедленно]],
            [#text(size: 10pt, weight: "bold")[активно]],
        )
        \
        #text(size: 12pt, weight: "bold")[О выполнении настоящего предписания прошу сообщить по
        каждому пункту \ согласно сроку устранения письменно.]
        \
        \
        #align(left)[
        Предписание выдал: \ \
        дата:#h(0.5cm) 06.06.2025 #h(0.5cm)
        подпись:#h(2cm) Максим
        РуководительООТПБиООС
        ]
        \
        #align(left)[
        Контроль устранения нарушений провел: \ \
        дата:#h(3cm)
        подпись:#h(2cm) 
        // Максим
        // РуководительООТПБиООС
        ]