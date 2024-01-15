<?php

namespace App\Models;

use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class Inspector extends Model
{
	use HasDateTimeFormatter;
    use SoftDeletes;

    public function department(): BelongsTo
    {
        return $this->belongsTo(Department::class);
    }
    }
