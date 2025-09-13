interface DashboardBoxProps {
  title: string;
  icon: string;
  onClick: () => void;
}

export default function DashboardBox({ title, icon, onClick }: DashboardBoxProps) {
  return (
    <div
      onClick={onClick}
      className="bg-white p-6 rounded-lg shadow cursor-pointer hover:shadow-lg transition"
    >
      <div className="text-5xl mb-4">{icon || "🌾"}</div>
      <div className="text-lg font-semibold text-gray-800 hover:text-green-700">{title}</div>
    </div>
  );
}
