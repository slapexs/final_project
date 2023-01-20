import clientPromise from "../../lib/mongodb"

export default async function handler(req, res) {
	const { amount } = req.query
	const client = await clientPromise
	const db = client.db("final_project")
	switch (req.method) {
		case "GET":
			const countComapny = await db
				.collection("companies")
				.find({})
				.sort({})
				.toArray()
			const listId = []
			for (let i = 0; i < amount; i++) {
				listId.push(Math.floor(Math.random() * countComapny.length))
			}
			listId.sort((a, b) => a - b)

			const listCompany = []
			for (let i = 0; i < listId.length; i++) {
				listCompany.push(countComapny[listId[i]])
			}
			res.json({ listCompany })
			break

		default:
			res.json({ status: "Request error, please use GET method only." })
			break
	}
}
