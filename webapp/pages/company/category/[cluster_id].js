import Head from "next/head"

// Components
import ViewCompany from "../../../components/ViewCompany"
const clusters = [
	"Data",
	"Other",
	"Online marketing",
	"Software",
	"Hardware",
	"Network",
	"IT",
]

export async function getServerSideProps(context) {
	const { cluster_id } = context.query
	const res = await fetch(
		`http://localhost:3000/api/getcompany?cluster=${cluster_id}`
	)
	const data = await res.json()
	return { props: { companies: data.data, cluster_id } }
}

const CompanyDetail = ({ companies, cluster_id }) => {
	return (
		<>
			<Head>
				<title>สถานประกอบการหมวดหมู่ | {clusters[cluster_id]}</title>
				<meta
					name="description"
					content="ระบบแนะนำบริษัทสำหรับฝึกงานตามความสนวจ ด้วยเทตโนโลยีปัญญาประดิษฐ์ | Recommended System of Internship's Company"
				/>
				<meta name="viewport" content="width=device-width, initial-scale=1" />
				<link rel="icon" href="/houseparty.png" />
			</Head>

			<ViewCompany name={clusters[cluster_id]} companies={companies} />
		</>
	)
}

export default CompanyDetail
