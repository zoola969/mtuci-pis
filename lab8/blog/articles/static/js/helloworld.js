const groupmates = [
	{
		name: "Иванов Алексей",
		group: "БСТ-2301",
		age: 19,
		marks: [5, 4, 5, 4, 5],
	},
	{ name: "Петрова Мария", group: "БСТ-2302", age: 18, marks: [4, 5, 5, 5, 4] },
	{
		name: "Сидоров Дмитрий",
		group: "БСТ-2301",
		age: 20,
		marks: [3, 4, 3, 4, 3],
	},
	{ name: "Козлова Анна", group: "БСТ-2302", age: 19, marks: [5, 5, 4, 5, 5] },
	{
		name: "Морозов Кирилл",
		group: "БСТ-2301",
		age: 18,
		marks: [4, 3, 4, 3, 4],
	},
	{
		name: "Новикова Елена",
		group: "БСТ-2302",
		age: 19,
		marks: [5, 4, 4, 5, 4],
	},
	{ name: "Волков Артём", group: "БСТ-2301", age: 20, marks: [3, 3, 4, 3, 3] },
	{
		name: "Соколова Дарья",
		group: "БСТ-2302",
		age: 18,
		marks: [4, 5, 4, 4, 5],
	},
	{
		name: "Лебедев Максим",
		group: "БСТ-2301",
		age: 19,
		marks: [5, 5, 5, 4, 5],
	},
	{
		name: "Кузнецова Ольга",
		group: "БСТ-2302",
		age: 20,
		marks: [4, 4, 3, 4, 4],
	},
];

console.log(groupmates);

document.addEventListener("DOMContentLoaded", () => {
	const printStudents = (students) => {
		console.log(
			"Имя студента".padEnd(15),
			"Группа".padEnd(8),
			"Возраст".padEnd(8),
			"Оценки".padEnd(20),
		);
		// был выведен заголовок таблицы
		for (let i = 0; i <= students.length - 1; i++) {
			// в цикле выводится каждый экземпляр студента
			console.log(
				students[i].name.padEnd(15),
				students[i].group.padEnd(8),
				String(students[i].age).padEnd(8),
				String(students[i].marks).padEnd(20),
			);
		}
		console.log("\n"); // добавляется пустая строка в конце вывода
	};
	const filterByGroup = (students, groupName) => {
		return students.filter((student) => student.group === groupName);
	};

	console.log("Все студенты:");
	printStudents(groupmates);

	console.log("Отфильтрованные студенты (БСТ-2302):");
	printStudents(filterByGroup(groupmates, "БСТ-2302"));
});
