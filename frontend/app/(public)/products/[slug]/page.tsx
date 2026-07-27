export default function ProductDetailPage({ params }: { params: { slug: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Product: {params.slug}</h1>
      <p className="mt-2 text-sm text-gray-600">Product details go here.</p>
    </div>
  );
}
