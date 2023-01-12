import { useRouter } from "next/router"
import Head from "next/head"

// Components
import ViewCompany from "../../../components/ViewCompany"

const CompanyDetail = () => {
	const router = useRouter()
	const { name } = router.query

	return (
		<>
			<Head>
				<title>{name} | หมวดหมู่สถานประกอบการ</title>
				<meta
					name="description"
					content="ระบบแนะนำบริษัทสำหรับฝึกงานตามความสนวจ ด้วยเทตโนโลยีปัญญาประดิษฐ์ | Recommended System of Internship's Company"
				/>
				<meta name="viewport" content="width=device-width, initial-scale=1" />
				<link rel="icon" href="/houseparty.png" />
			</Head>

			<ViewCompany name={name} />
		</>
	)
}

export default CompanyDetail
