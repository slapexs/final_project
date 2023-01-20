import Link from "next/link"

const PageNotFound = () => {
	return (
		<>
			<div className="w-full py-24 sm:py-20 flex justify-center h-screen">
				<div className="text-center h-full flex-col justify-between flex">
					<div>
						<h1 className="text-2xl text-gray-400">Page Not Found</h1>
					</div>
					<div>
						<h1 className="text-9xl font-bold">404</h1>
					</div>
					<div>
						<h1>
							<Link href={"/"} className="text-blue-400">
								กลับหน้าแรก
							</Link>
						</h1>
					</div>
				</div>
			</div>
		</>
	)
}

export default PageNotFound
