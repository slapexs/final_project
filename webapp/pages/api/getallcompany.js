import clientPromise from "../../lib/mongodb"

export default async function handler(req, res) {
	const client = await clientPromise
	const db = client.db("final_project")

	switch (req.method) {
		case "GET":
			const allCompanies = await db
				.collection("companies")
				.find({})
				.sort({ short_company: 1 })
				.toArray()
			res.json({ status: 200, data: allCompanies })
			break
	}
}
