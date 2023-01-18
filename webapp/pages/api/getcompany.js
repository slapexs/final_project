import clientPromise from "../../lib/mongodb"

export default async function handler(req, res) {
	const client = await clientPromise
	const db = client.db("final_project")
	const { cluster } = req.query

	switch (req.method) {
		case "GET":
			const allPosts = await db
				.collection("companies")
				.find({ cluster: cluster })
				.toArray()
			res.json({ status: 200, data: allPosts })
			break
	}
}
